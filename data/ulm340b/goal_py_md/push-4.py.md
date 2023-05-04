

I look forward to your response.[eod] [code]using System;
using System.Linq;
using System.Drawing;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Text;
using System.Windows.Forms;

namespace CSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rect = new Rectangle(100, 50, 200, 200);
            e.Graphics.FillRectangle(Brushes.Red, rect);
            Rectangle rect2 = new Rectangle(rect.X, rect.Y, rect.Width, rect.Height);
            e.Graphics.FillRectangle(Brushes.Blue, rect2);

            string txt = "Hello world!";
            Font _font = new Font("Arial", 25);
            e.Graphics.DrawString(txt, _font, Brushes.White, rect);

            e.Graphics.DrawRectangle(new Pen(Color.BlueViolet), rect);
            e.Graphics.DrawEllipse(new Pen(Color.DarkBlue), rect2);

            GraphicsPath gp = new GraphicsPath();
            gp.AddPolygon(new Point[] { new Point(0, 0), new Point(300, 0),
                new Point(150, 300) });
            e.Graphics.DrawPath(Pens.Black, gp);

            gp.CloseAllFigures();

            Image img = Image.FromFile("logo.png");
            Rectangle imgRect = new Rectangle(img.Width, img.Height);
            e.Graphics.DrawImage(img, imgRect);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = this.CreateGraphics();
            g.Clear(this.BackColor);
            this.Invalidate();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Graphics g = this.CreateGraphics();
            string text = "Hello world!";
            g.DrawString(text, new Font("Arial", 14, FontStyle.Bold), Brushes.Black, 10, 20);
            this.Invalidate();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Graphics g = this.CreateGraphics();
            Rectangle rect = new Rectangle