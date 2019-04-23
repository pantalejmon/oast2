# EvolutionaryAlgorithmOAST

## Main.py 
Zostawiony na implementację do odpalania programu
## Models.py - wszystkie modele do parsera i algorytmu ewolucyjnego
- Link
- Demand
- DemandPath
- Gene
- Chromosome
## Parser.py
Przed parsowaniem plik z danymi jest dzielony na 2 części według znaku podziału (**-1**)
- **get_links_list_from_file(__net_string_links)** - zwraca listę obiektów Link; **__net_string_links** - pierwsza część pliku z danymi (do liczby -1)
- **get_demands_from_file(__net_string_demands)** - zwraca listę obiektów Demand; **__net_string_demands** - druga część pliku z danymi (po liczbie -1)
- **get_number_of_links(__net_string_links)** - zwraca liczbę Links podaną w pierwszej części pliku
- **get_number_of_demands(__net_string_demands)** - zwraca liczbę Demands podaną w drugiej części pliku z danymi
## net4.txt, net12_1.txt, net12_2.txt
Skopiowane pliki z danymi ze strony przedmiotu

## Nazewnictwo z wykładu (+ jedna dodatkowa nazwa - allele)
![Zrzut ekranu 2019-04-23 o 11 25 00](https://user-images.githubusercontent.com/31706606/56570450-473d4c00-65bb-11e9-9909-99b460471a70.png)
