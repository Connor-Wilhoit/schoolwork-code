#include <iostream>
#include <ctime>
#include <cstdlib>
#include <fstream>
const int SIM_SIZE = 1000;
const int AVG = SIM_SIZE;
using namespace std;
int main()
{
	srand(time(0));
	int distribution[SIM_SIZE][3];
	int average[AVG];
	ofstream fout;
	fout.open("simulation_data.txt");	

	for(int person=0; person<SIM_SIZE; person++)
	{
		for(int pick=1, roll=0; pick < 4; pick++, roll++)
		{
			int p = (rand() % 8) + 1;
			distribution[person][roll] = p;

		}
		average[person] = (distribution[person][0] + distribution[person][1] + distribution[person][2])/3;

	}

	for(int i=0; i<SIM_SIZE; i++)
	{
		for(int p=0;p<3;p++)
		{
			fout << "distribution[" << i << "][" << p << "] = " << distribution[i][p] << endl;
			//fout << "average[" << i << "] = " << average[i] << endl;
		}
		fout << "average[" << i << "] = " << average[i] << endl;
	}


	fout.close();
	return 0;
}
