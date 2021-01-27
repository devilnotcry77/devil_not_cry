public DataTable Select(String sql) {
    MySqlBaseConnectionStringBuilder builder  = new MySqlBaseConnectionStringBuilder()
    builder.Server = "192.168.201.10";
    builder.Port = 3306; 
    builder.Database = "testuser_test";
    builder.UserID = "testuser";
    builder.Password = "test123";
    builder.CharacterSet = "utf8";

    MySqlConnection connect = new MySqlConnection(builder.ConnectionString);
    MySqlConnection command = new MySqlCommand(sql, connect);

    try
    {
        connect.Open();
        DataTable table = DataTable();
        table.Load(command.ExecuiteReader());

        return table;

    }
    catch (System.Exception)
    {
        
         MessageBox.Show("Error!");

         return();

             }
}