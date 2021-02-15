public partial class Form16 : Form
    {
        public Form16()
        {
            InitializeComponent();
            timer1.Interval = 10000;
            timer1.Start();
        }

        private void Form16_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Form24 frm = new Form24();
            frm.Show();
            timer1.Stop();
            Hide();
        }
