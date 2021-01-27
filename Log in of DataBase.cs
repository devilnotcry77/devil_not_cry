private void button1_Click(object sender, EventArgs e)
        {
 
            //SqlConnection con = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Database1.mdf;Integrated Security=True");
            // SqlDataAdapter sda = new SqlDataAdapter("Select Count(*) From admin Where login='" + textBox1.Text + "' and password = '" +textBox2.Text + "'",con);
            // DataTable dt = new DataTable();
            // sda.Fill(dt);
            //if (dt.Rows[0][0].ToString() == "1")
            // {
            //     this.Hide();
            //     Form2 f2 = new Form2();
            //     f2.Show();
            // }
            // else
            // {
            //     MessageBox.Show("Пожалуйста, проверьте правильность введенных данных!");
            // }
 
            string Connect = "server=localhost;user id=admin;password=admin;persistsecurityinfo=True;database=project";
            string CommandText = "SELECT Count(*) FROM  admin WHERE login = '" + textBox1.Text + "' AND password = '" + textBox2.Text + "' LIMIT 1";
            MySqlConnection myConnection = new MySqlConnection(Connect);
            MySqlCommand myCommand = new MySqlCommand(CommandText, myConnection);
            myConnection.Open();
            myCommand.ExecuteNonQuery();
            MySqlDataAdapter dataAdapter = new MySqlDataAdapter(myCommand);
            DataTable dt = new DataTable();
            dataAdapter.Fill(dt);
            if (dt.Rows[0][0].ToString() == "1")
            {
                 this.Hide();
                 Form2 f2 = new Form2();
                 f2.Show();
            }
            else
            {
                 MessageBox.Show("Пожалуйста, проверьте правильность введенных данных!");
            }
 
        }