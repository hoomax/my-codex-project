using Xunit;
using CalculatorLib;

namespace CalculatorTests
{
    public class CalculatorTests
    {
        [Fact]
        public void Add_Works()
        {
            var calc = new Calculator();
            Assert.Equal(5, calc.Add(2, 3));
        }

        [Fact]
        public void Divide_ByZero_Throws()
        {
            var calc = new Calculator();
            Assert.Throws<DivideByZeroException>(() => calc.Divide(1, 0));
        }
    }
}
