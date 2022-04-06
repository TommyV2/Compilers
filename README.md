# Compilers

## Antlr command for generating files:

java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 MyGrammer.g4 -visitor -o dist

## To generate tree:

_to najlepiej w nowym folderze robic ze skopiwaną gramatyką i plikiem wejściowym_

java -jar antlr-4.9.2-complete.jar MyGrammer.g4

javac  MyGrammer*.java 

java -cp .;antlr-4.9.2-complete.jar org.antlr.v4.runtime.misc.TestRig MyGrammer start test.xd -gui

_start = start command w gramatyce_
