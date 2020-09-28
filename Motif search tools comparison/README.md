# Сравнение точности определения мотивов транскриционного фактора MAFF различными сервисами и программными пакетами.
Транскрипционный фактор в виде файла bed (narrowpeak) загружен с https://www.encodeproject.org/search/?type=Experiment&status=released  

В каждой строке прописаны регионы человеческого генома, обогащённые данным транскриционным фактором.
- Сортировка bed файла с наилучшими q-value, выборка топ 1000, сохранение в fasta формате:
 
![GitHub Logo](images/Рисунок59.png)
![GitHub Logo](images/Рисунок60.png)
 
Factorbook:

![GitHub Logo](images/Рисунок61.png)

Jaspar:
 
![GitHub Logo](images/Рисунок62.png)
![GitHub Logo](images/Рисунок63.png)
![GitHub Logo](images/Рисунок64.png)
 
Сгенерированный background с сохранение тринуклеотидов:
 
![GitHub Logo](images/Рисунок65.png)

RSAT (с программным background):
 
![GitHub Logo](images/Рисунок66.png)
![GitHub Logo](images/Рисунок67.png)
![GitHub Logo](images/Рисунок68.png)
![GitHub Logo](images/Рисунок69.png)
![GitHub Logo](images/Рисунок70.png)
 
 
RSAT (со сгенерированным background)
 
![GitHub Logo](images/Рисунок71.png)
![GitHub Logo](images/Рисунок72.png)
![GitHub Logo](images/Рисунок73.png)
![GitHub Logo](images/Рисунок74.png)
![GitHub Logo](images/Рисунок75.png)

 
Унификация названия последовательностей в fasta файле для MEME (иначе не принимает):
+ применение алгоритма цепей Маркова для преобразования бэкграунда (иначе MEME не принимает):

![GitHub Logo](images/Рисунок76.png)

(последняя подчеркнутая строчка относится к алгоритму Homer)
MEME-chip (с программным BG)

![GitHub Logo](images/Рисунок77.png)
 
MEME-chip (со сгенерированным бг)

![GitHub Logo](images/Рисунок78.png)

Homer (с программным BG):

![GitHub Logo](images/Рисунок79.png)

Homer (со сгенерированным BG):

![GitHub Logo](images/Рисунок80.png)

Вывод:
Наилучшим образом с поиском мотивов справился RSAT с предоставленным программой бэкграундом. Это можно понять исходя из того, что у него больше всего найденных мотивов подходит к мотивам в Jaspar и Factorbook. Основные схожести по таким мотивам как: “*tcagca*”, “*tgctga**tcagca*”
Хуже всех справился Homer, так как с любыми бэкграундами нашёл только по одному мотиву и то, основная его часть (по частоте) не до конца совпадает по первому нуклеотиду.
Также у RSAT числа e-value более приближенные к Factorbook и Jaspar.


