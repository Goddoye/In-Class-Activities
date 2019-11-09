var x = 15
var y = 20
// Checks if one value is equal to another
if (x === y)
{
console.log(`Your x value is equal to your y value`)
}
else 
{
console.log(`Your x value is not equal to your y value`)

}
// Checks if one value is NOT equal to another
if (x !== y)
{
console.log(`Your x value is not equal to your y value`)
}
else
{
console.log(`Your x value is equal to your y value`)
}
// Checks if one value is less than another
if (x < y)
{
console.log(`Your x value is less than your y value`)
}
else
{
console.log(`Your x value is greater than your y value`)
}
// Checks if one value is greater than another
if (x > y)
{
    console.log(`Your x value is greater than your y value`)
}
else
{
    console.log(`Your y value is greater than your x value`)
}
// Checks if a value is less than or equal to another
if (x<=y)
{
    console.log(`Your x value is less than or equal to your y value`)
}
else
{
    console.log(`Your x value is greater than your y value`)
}
// Checks for two conditions to be met using &&
if (x===15 && y===20)
{
    console.log(`Both your vaules returned true`)
}
else
{
    console.log(`One or both of your vaules returned false`)
}
// Checks if either of two conditions is met using ||
if (x>15 || y===20)
{
    console.log(`At least one of your vaules returned true`)
}

// Nested if statements
if (x>10){
    if (y <15){
        console.log(`Your x value is greater than 10 and your y value is less than 15`)
    }
    else if (y=== 20){
        console.log(`Your x value is greater than 10 and your y value is equal to 20`)
    }
    else{
        console.log(`Your x value is greater than 10 and your y value is greater than 15 but not equal to 20`)
    }
}
