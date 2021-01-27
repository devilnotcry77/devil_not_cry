\\ Èç ïàïêè "Resurese"
public Form1()
        {
            InitializeComponent();
                img = Resource.Kuri_1680x1050;
        this.BackgroundImage = new Bitmap( img );
    }
}
\\×åðåç ïóòü 
public MainForm() {
  InitializeComponent();
  this.BackgroundImage = new Bitmap(@"C:\WINDOWS\Web\Wallpaper\Kuri_1680x1050");// ïóòü ê èçîáðàæåíèþ
}
\\Åù¸ îäèí ñïîñîá
 this.BackgroundImage = new Bitmap(@"d:\ôîòî\img247.jpg");
            this.BackgroundImageLayout = ImageLayout.Stretch;
