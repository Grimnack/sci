set title ""
set xlabel "Tick"
set ylabel "Nombre de poissons (bleu) et requins (rouge)"

plot "courbe.txt" using 1:2  with linespoints lt rgb "blue" title '', "courbe.txt" using 1:3  with linespoints lt rgb "red" title ''