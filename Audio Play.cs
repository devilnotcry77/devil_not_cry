Audio sp;
 
        private void Form1_Load(object sender, EventArgs e)
        {
            sp = new Audio(@"E:\Sound.mp3");
        }
 
        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "Play")
            {
                sp.Play();
                button1.Text = "Stop";
            }
            else
            {
                sp.Pause();
                button1.Text = "Play";
            }
        }