class Method 
{
    public string GetPass()
    {
        Random rnd = new Random();
        string Password = "";

        for (int i = 0; i < 16; i++)
        {
            Password += (char)rnd.Next('a', 'z');
        }
        return Password;
    }
}

private void button1_Click(object sender, EventArgs e)
{
    Method P = new Method();
    var password = P.GetPass();
    textBox1.Text = password;
}
