namespace DbExample
{
    public partial class Form1 : Form 
    {
        public Form1()
        {
            InitializeComponent();
            dataGridView1.DataSourse = DbConnection.Select("SELECT * FROM 'users'");
        }
    }
}