#Мережа відстаней між основними містами Європи
# Починаємо з  міста Київ 


# cities = ["Kyiv",  "Warsaw", "Berlin","Vienna" , "Bern", "Madrid" ]
graph = {
    "Kyiv": {"Warsaw": 690, "Berlin": 1200, "Vienna": 1200},
    "Warsaw": {"Kyiv": 690, "Berlin": 570, "Vienna": 680, "Madrid": 2290},
    "Berlin": {"Kyiv": 1200, "Warsaw": 570, "Vienna": 670, "Bern": 750},
    "Vienna": {"Kyiv": 1200, "Berlin": 670, "Warsaw": 680, "Bern": 810, "Madrid": 2860},
    "Bern": {"Vienna": 810, "Madrid": 1250},
    "Madrid": {"Warsaw": 2290, "Bern": 1250}
}
