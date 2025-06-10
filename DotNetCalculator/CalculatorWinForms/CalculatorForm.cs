using System;
using System.Windows.Forms;
using CalculatorLib;

namespace CalculatorWinForms
{
    public class CalculatorForm : Form
    {
        private TextBox inputA;
        private TextBox inputB;
        private ComboBox operationBox;
        private Button computeButton;
        private Label resultLabel;
        private Calculator calculator = new Calculator();

        public CalculatorForm()
        {
            Text = "Calculator";
            Width = 300;
            Height = 200;

            inputA = new TextBox { Left = 20, Top = 20, Width = 100 };
            inputB = new TextBox { Left = 160, Top = 20, Width = 100 };
            operationBox = new ComboBox { Left = 20, Top = 60, Width = 240 };
            operationBox.Items.AddRange(new string[] { "add", "sub", "mul", "div" });
            operationBox.SelectedIndex = 0;

            computeButton = new Button { Left = 20, Top = 100, Width = 240, Text = "Compute" };
            computeButton.Click += OnCompute;

            resultLabel = new Label { Left = 20, Top = 140, Width = 240 };

            Controls.Add(inputA);
            Controls.Add(inputB);
            Controls.Add(operationBox);
            Controls.Add(computeButton);
            Controls.Add(resultLabel);
        }

        private void OnCompute(object sender, EventArgs e)
        {
            if (double.TryParse(inputA.Text, out double a) &&
                double.TryParse(inputB.Text, out double b))
            {
                double result = operationBox.SelectedItem.ToString() switch
                {
                    "add" => calculator.Add(a, b),
                    "sub" => calculator.Subtract(a, b),
                    "mul" => calculator.Multiply(a, b),
                    "div" => calculator.Divide(a, b),
                    _ => 0
                };

                resultLabel.Text = $"Result: {result}";
            }
            else
            {
                MessageBox.Show("Invalid input");
            }
        }
    }
}
