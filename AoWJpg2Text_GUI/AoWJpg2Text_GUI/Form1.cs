using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace AoWJpg2Text_GUI
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_DragDrop(object sender, DragEventArgs e)
        {

        }

        private void MainForm_DragEnter(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.Copy;
        }

        private void textBox1_DragDrop(object sender, DragEventArgs e)
        {
            string[] fileName =
                (string[])e.Data.GetData(DataFormats.FileDrop, false);

            // Jpg2Text
            string currentDir = System.IO.Path.GetDirectoryName(Application.ExecutablePath);
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = System.IO.Path.Combine(currentDir, "jpg2text.exe");
            pInfo.Arguments = fileName[0];
            Process p = Process.Start(pInfo);
            p.WaitForExit();


            System.IO.StreamReader sr = new System.IO.StreamReader(
                 System.IO.Path.Combine(currentDir,"out.txt"),Encoding.GetEncoding("utf-8"));
            string result_text = sr.ReadToEnd();
            sr.Close();

            textBox1.Text = result_text;
        }

        private void textBox1_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.Copy;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }
    }
}
