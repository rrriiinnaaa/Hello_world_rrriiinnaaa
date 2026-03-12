read -p "Введите вес (кг): " WEIGHT
read -p "Введите рост (см): " HEIGH

HEIGHT_M=$((HEIGHT * HEIGHT))
BMI=$((WEIGHT * 10000 / HEIGHT_M))

echo "Ваш вес: $WEIGHT кг"
echo "Ваш рост: $HEIGHT см"
echo "Ваш ИМТ: $BMI"
