//Для записи на карту Mifare вы, прежде всего, должны иметь корректное значение ключа (что играет защитную роль), а также успешно пройти аутентификацию.

<manifest xmlns:android="http://schemas.android.com/apk/res/android"  
	    package="org.reno"  
	    android:versionCode="1"  
	    android:versionName="1.0" >   
	    <uses-permission android:name="android.permission.NFC" />   
	    <uses-sdk android:minSdkVersion="14" />   
	    <uses-feature android:name="android.hardware.nfc" android:required="true" />   
	    <application  
	        android:icon="@drawable/ic_launcher"  
	        android:label="@string/app_name" >   
	        <activity  
	            android:name="org.reno.Beam"  
	            android:label="@string/app_name"  
	            android:launchMode="singleTop" >   
	            <intent-filter>   
	                <action android:name="android.intent.action.MAIN" />   
	    
	                <category android:name="android.intent.category.LAUNCHER" />   
	            </intent-filter>   
	            <intent-filter>   
	                <action android:name="android.nfc.action.TECH_DISCOVERED" />   
	            </intent-filter>   
	            <meta-data  
	                android:name="android.nfc.action.TECH_DISCOVERED"  
	                android:resource="@xml/nfc_tech_filter" />   
	        </activity>  
	    </application>   
    </manifest>

    //res/xml/nfc_tech_filter.xml：

    <resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2"> 
	    <tech-list> 
	       <tech>android.nfc.tech.MifareClassic</tech> 
	    </tech-list> 
    </resources>
    
    //Пример того, как читать карту MifareClassic:

    private void processIntent(Intent intent) {    
	    Tag tagFromIntent = intent.getParcelableExtra(NfcAdapter.EXTRA_TAG);   
	    for (String tech : tagFromIntent.getTechList()) {   
	        System.out.println(tech);   
	    }   
	    boolean auth = false;   
	    MifareClassic mfc = MifareClassic.get(tagFromIntent);   
	    try {   
	        String metaInfo = "";   
	        //Enable I/O operations to the tag from this TagTechnology object.   
	        mfc.connect();   
	        int type = mfc.getType(); 
	        int sectorCount = mfc.getSectorCount();   
	        String typeS = "";   
	        switch (type) {   
	        case MifareClassic.TYPE_CLASSIC:   
	            typeS = "TYPE_CLASSIC";   
	            break;   
	        case MifareClassic.TYPE_PLUS:   
	            typeS = "TYPE_PLUS";   
	            break;   
	        case MifareClassic.TYPE_PRO:   
	            typeS = "TYPE_PRO";   
	            break;   
	        case MifareClassic.TYPE_UNKNOWN:   
	            typeS = "TYPE_UNKNOWN";   
	            break;   
	        }   
	        metaInfo += "Card type：" + typeS + "n with" + sectorCount + " Sectorsn, "  
	                + mfc.getBlockCount() + " BlocksnStorage Space: " + mfc.getSize() + "Bn";   
	        for (int j = 0; j < sectorCount; j++) {   
	            //Authenticate a sector with key A.   
	            auth = mfc.authenticateSectorWithKeyA(j,   
	                    MifareClassic.KEY_DEFAULT);   
	            int bCount;   
	            int bIndex;   
	            if (auth) {   
	                metaInfo += "Sector " + j + ": Verified successfullyn";   
	                bCount = mfc.getBlockCountInSector(j);   
	                bIndex = mfc.sectorToBlock(j);   
	                for (int i = 0; i < bCount; i++) {   
	                    byte[] data = mfc.readBlock(bIndex);   
	                    metaInfo += "Block " + bIndex + " : "  
	                            + bytesToHexString(data) + "n";   
	                    bIndex++;   
	                }   
	            } else {   
	                metaInfo += "Sector " + j + ": Verified failuren";   
	            }   
	        }   
	        promt.setText(metaInfo);   
	    } catch (Exception e) {   
	        e.printStackTrace();   
	    }   
    }
    
    