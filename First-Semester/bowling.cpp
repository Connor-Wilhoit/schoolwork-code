#include <iostream>
#include <cstring>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cctype>
#include <cstddef>
using namespace std;
void CleanFile(ifstream &fin, ofstream &fout, char &score);
void ReadPins(ifstream &Fin, int PinArray[], int &size, int &i);
void ScoreGame(int *&pin_array, int &index, int &frame, int &total_score);
int main()
{
	ifstream fin;
	ofstream fout;
	char score;
	int *pin_array, index, frame, total_score;
	CleanFile(fin, fout, score);
	ScoreGame(pin_array, index, frame, total_score);
	return 0;
}
void CleanFile(ifstream &fin, ofstream &fout, char &score)
{
	fin.open("lane9.txt");
	fout.open("cleanlane9.txt");
	if(fin.fail())
	{
		cout << "Error opening file" << endl;
		exit(1);
	}
	while(fin.get(score))
	{		
		if((isdigit(score)) || (isspace(score)))
		{
			fout.put(score);
		}

	}
	fin.close();
	fout.close();
}
void ReadPins(ifstream &Fin, int PinArray[], int &size, int &i)
{
	Fin.open("cleanlane9.txt");
	if(Fin.fail())
	{
		cout << "Error opening file" << endl;
		exit(1);
	}
	i=0;
	while(Fin >> size)
	{
		PinArray[i] = size;
		i++;	
	}
	
	Fin.close();
}
void ScoreGame(int *&pin_array, int &index, int &frame, int &total_score)
{
	ifstream Fin;
	int pinArray[23], size, i;
	ReadPins(Fin, pinArray, size, i);
	pin_array = pinArray;
	index = i;
	frame = 1;
	total_score = 0;
	int n = 0;
	while(frame < 10)
	{
		if((pin_array[n] < 10) && ((pin_array[n] + pin_array[n+1])<10))			//less than 10 pins
		{

			cout << "	 " << frame << "	     \n"
		     	     << "********************\n"
		     	     << "*   " << pin_array[n] << "   \t[" << pin_array[n+1] << "]*\n"
		     	     << "*		   *\n"
		     	     << "*		   *\n"
		     	     << "*		   *\n"
		     	     << "*		   *\n"
		     	     << "*		   *\n";
			total_score += (pin_array[n] + pin_array[n+1]);
			cout << "*       " << total_score << "    \t   *\n"
		     	     << "*		   *\n"
		     	     << "********************" << endl;
			n += 2;
			frame++;		
		}
		else if((pin_array[n] < 10) && ((pin_array[n] + pin_array[n+1]) == 10))		//spare
		{
			cout << "        " << frame << "           \n"
			     << "********************\n"
			     << "*  " << pin_array[n] << "      \t[" << pin_array[n+1] << "]*\n"
			     << "*                  *\n"
			     << "*                  *\n"
			     << "*                  *\n"
			     << "*                  *\n"
			     << "*                  *\n";
			total_score += (pin_array[n] + pin_array[n+1] + pin_array[n+2]);
			cout << "*       " << total_score << "    \t   *\n"
			     << "*                  *\n"
			     << "********************" << endl;
			n += 2;
			frame++;
		}
		else										//strike
		{
			cout << "        " << frame << "             \n"
			     << "********************\n"
			     << "*  " << pin_array[n] << "      \t[X]*\n"
			     << "*                  *\n"
			     << "*                  *\n"
			     << "*                  *\n"
			     << "*                  *\n"
			     << "*                  *\n";
			total_score += (pin_array[n] + pin_array[n+1] + pin_array[n+2]);
			cout << "*      " << total_score << "    \t   *\n"
			     << "*                  *\n"
			     << "********************" << endl;
			n++;
			frame++;
		}

	}
	while(frame == 10)
	{
		if((pin_array[n] == 10) && (pin_array[n+1] < 10))
		{
			cout << "       " << frame << "              \n"
			     << "*********************\n"
			     << "*  " << pin_array[n] << "      [X][" << pin_array[n+1] << "][" << pin_array[n+2] << "]*\n"
			     << "*                   *\n"
			     << "*                   *\n"
			     << "*                   *\n"
			     << "*                   *\n"
			     << "*                   *\n";
			total_score += ((pin_array[n] + pin_array[n+1] + pin_array[n+2]) + (pin_array[n+1]) + (pin_array[n+2]));
			cout << "*      " << total_score << "   \t    *\n"
			     << "*                   *\n"
			     << "*********************" << endl;
			frame++;
		}
	}

}
