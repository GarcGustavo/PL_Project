MAPINATOR

Mapinator is a simple and easy to use map creation language. Utilizing the Unity engine and python, it produces a simple procedurally generated map with customizable parameters. 

Once the language is used to create a desired map, it generates C# scripts that can be run and rendered using the Unity game engine. 
The main goal of this language is to make map creation and game development more accessible to creators, allowing people to code complex map algorithms with a few simple commands. 

The functions and properties that the language can create and edit means game-makers are free to focus on more important tasks, letting the language do most of the complex scripting work.

Language Tutorial Video: 

[Tutorial Video](https://www.youtube.com/watch?v=0ygKaT88NQs)

Instructions:

Setting up Mapinator: 

Install Python 3.

Install JetBrain’s Pycharm. 

Install Unity. 

Download PL_Project.zip from the GitHub page.

Extract all the files.

Running Mapinator: 

Open the folder PL_Project in JetBrain’s Pycharm IDE. 

Search for the text file called “MapinatorCode.txt” and write your code there. 

When the code is ready, run the MainClass.py.

Search for the “output” folder and import all the scripts to Unity. 

Language Reference Manual: 

Commands: 

1- GenerateMap map_name: Creates a map with the specified name.

2- SetMapSize map_name number number: Creates a map with the specified size. 

3- SetSeed map_name number: Creates a random id used to generate the noise map. 

4- SetLacunarity map_name number: It is a value to controls distance between peaks. 

5- SetDetails map_name number: It is a value to controls the level of details to show the map. 

6- SetHeightMult map_name number: It is a value to controls the general height of the map.

7- SetNoiseScale map_name number: it is the scale to represent the map in a flat plane.

8- SetNoiseDensity map_name number: It is a value to control how elevations are distributed or clumped together.

9- SetPersistence map_name number: It is a value to control how higher values affect the map.

10- GenerateCode map_name: Command need to finalize the code.
