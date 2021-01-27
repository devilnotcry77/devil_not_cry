//AndroidManifest.xml:

<uses-permission android:name="android.permission.NFC" />
<uses-sdk android:minSdkVersion="10"/>

//In the onCreate function，you can apply the NfcAdapter：

public void onCreate(Bundle savedInstanceState) {
……
adapter = NfcAdapter.getDefaultAdapter(this);
……
}

//Следующий целевой вызов демонстрирует функцию чтения. Если широковещательное сообщение системы равняется NfcAdapter.ACTION_TAG_DISCOVERED, 
//тогда вы можете считать информацию и показать ее.

@Override
	    protected void onNewIntent(Intent intent){
	        if(NfcAdapter.ACTION_TAG_DISCOVERED.equals(intent.getAction())){
	        mytag = intent.getParcelableExtra(NfcAdapter.EXTRA_TAG);  // get the detected tag
	        Parcelable[] msgs =
	intent.getParcelableArrayExtra(NfcAdapter.EXTRA_NDEF_MESSAGES);
	            NdefRecord firstRecord = ((NdefMessage)msgs[0]).getRecords()[0];
	            byte[] payload = firstRecord.getPayload();
	            int payloadLength = payload.length;
	            int langLength = payload[0];
	            int textLength = payloadLength - langLength - 1;
	            byte[] text = new byte[textLength];
	            System.arraycopy(payload, 1+langLength, text, 0, textLength);
	            Toast.makeText(this, this.getString(R.string.ok_detection)+new String(text), Toast.LENGTH_LONG).show();
	                    }
        }

//Следующий код демонстрирует функцию записи. Перед тем, как определить значение mytag, вы должны убедиться, 
//что метка определена и только потом вписать в нее свои данные.

If (mytag==Null){
    ……
}
else{
……
write(message.getText().toString(),mytag);
……
}
    private void write(String text, Tag tag) throws IOException, FormatException {
        NdefRecord[] records = { createRecord(text) };
        NdefMessage  message = new NdefMessage(records);
// Get an instance of Ndef for the tag.
        Ndef ndef = Ndef.get(tag); // Enable I/O
        ndef.connect(); // Write the message
        ndef.writeNdefMessage(message); // Close the connection
        ndef.close();
    }
    
//В зависимости от прочитанной информации вы можете выполнить дополнительные действия, такие как запуск какого-либо задания, переход по ссылке и т.д.

