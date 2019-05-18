#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;
const int SIM_NUM = 10000;
const int AVG = SIM_NUM;
void ball_vector(vector<int> &balls);
void work_space();
int main()
{
	work_space();
	return 0;
}
void ball_vector(vector<int> &balls)
{
	balls.push_back(1);
	balls.push_back(1);
	balls.push_back(1);
	balls.push_back(2);
	balls.push_back(2);
	balls.push_back(2);
	balls.push_back(3);
	balls.push_back(3);
	balls.push_back(3);
	balls.push_back(4);
	balls.push_back(4);
	balls.push_back(4);
	balls.push_back(5);
	balls.push_back(5);
	balls.push_back(5);
	balls.push_back(6);
	balls.push_back(6);
	balls.push_back(6);
	balls.push_back(7);
	balls.push_back(7);
	balls.push_back(7);
	balls.push_back(8);
	balls.push_back(8);
	balls.push_back(8);
}
void work_space()
{
	srand(time(0));
	vector<int> balls;
	int distribution[SIM_NUM][3];
	int tally_array[8] = {0};
	int draw_one=24, draw_two=23, draw_three=24;
	int roll_one=0, roll_two=1, roll_three=2;
	int q1, q2, q3;
	int sum=0;
	int mode;
	double real_average=0;
	double mean=0;
	ofstream fout;
	fout.open("simulation_data.txt");
	ball_vector(balls);
	random_shuffle(balls.begin(), balls.end() );

	for(int person=0; person < SIM_NUM; person++)
	{
		for(int pick=1; pick < 2; pick++)
		{
			int p = (rand() % draw_one);
			q1 = balls[p];
			distribution[person][roll_one] = balls[p];
			int temp = balls.at(p);
			balls.at(p) = balls.back();
			balls.back() = temp;
			balls.pop_back();
			switch(q1)
			{
				case 1:
					tally_array[0]++;
					break;
				case 2:
					tally_array[1]++;
					break;
				case 3:
					tally_array[2]++;
					break;
				case 4:
					tally_array[3]++;
					break;
				case 5:
					tally_array[4]++;
					break;
				case 6:
					tally_array[5]++;
					break;
				case 7:
					tally_array[6]++;
					break;
				case 8:
					tally_array[7]++;
					break;
			}

		}
		for(int pick=2; pick < 3; pick++)
		{
			int p = (rand() % draw_two);
			q2 = balls[p];
			distribution[person][roll_two] = balls[p];
			int temp = balls.at(p);
			balls.at(p) = balls.back();
			balls.back() = temp;
			balls.pop_back();
			switch(q2)
			{
				case 1:
					tally_array[0]++;
					break;
				case 2:
					tally_array[1]++;
					break;
				case 3:
					tally_array[2]++;
					break;
				case 4:
					tally_array[3]++;
					break;
				case 5:
					tally_array[4]++;
					break;
				case 6:
					tally_array[5]++;
					break;
				case 7:
					tally_array[6]++;
					break;
				case 8:
					tally_array[7]++;
					break;
			}

		}
		for(int pick=3; pick < 4; pick++)
		{
			int p = (rand() % draw_three);
			q3 = balls[p];
			distribution[person][roll_three] = balls[p];
			switch(q3)
			{
				case 1:
					tally_array[0]++;
					break;
				case 2:
					tally_array[1]++;
					break;
				case 3:
					tally_array[2]++;
					break;
				case 4:
					tally_array[3]++;
					break;
				case 5:
					tally_array[4]++;
					break;
				case 6:
					tally_array[5]++;
					break;
				case 7:
					tally_array[6]++;
					break;
				case 8:
					tally_array[7]++;
					break;
			}

		}
		balls.push_back(q1);
		balls.push_back(q2);
		random_shuffle(balls.begin(), balls.end() );

	}
	
	for(int i=0; i < SIM_NUM; i++)
	{
		for(int p=0; p < 3; p++)
		{
			fout << "distribution[" << i << "][" << p << "] = " << distribution[i][p] << endl;
		}
	}

	for(int i=0; i < SIM_NUM; i++)
	{
		sum = (distribution[i][0] + distribution[i][1] + distribution[i][2]);
		real_average += sum;
	}

	mean = (real_average/SIM_NUM);
	mode = *max_element(tally_array, tally_array+8);
	for(int i=0; i < 8; i++)
	{
		if(mode == tally_array[i])
		{
			fout << "tally_array[" << i << "] = mode (" << mode << ")" << endl;
			switch(i)
			{
				case 0:
					cout << "Yellow is the mode (most used)[" << mode << "] times" << endl;
					fout << "Yellow is the mode (most used)[" << mode << "] times" << endl;
					break;
				case 1:
					cout << "Blue is the mode (most used)[" << mode << "] times" << endl;
					fout << "Blue is the mode (most used)[" << mode << "] times" << endl;
					break;
				case 2:
					cout << "Red is the mode (most used)[" << mode << "] times" << endl;
					fout << "Red is the mode (most used)[" << mode << "] times" << endl;
					break;
				case 3:
					cout << "Purple is the mode (most used)[" << mode << "] times" << endl;
					fout << "Purple is the mode (most used)[" << mode << "] times" << endl;
					break;
				case 4:
					cout << "Orange is the mode (most used)[" << mode << "] times" << endl;
					fout << "Orange is the mode (most used)[" << mode << "] times" << endl;
					break;
				case 5:
					cout << "Green is the mode (most used)[" << mode << "] times" << endl;
					fout << "Green is the mode (most used)[" << mode << "] times" << endl;
					break;
				case 6:
					cout << "Maroon is the mode (most used)[" << mode << "] times" << endl;
					fout << "Maroon is the mode (most used)[" << mode << "] times" << endl;
					break;
				case 7:
					cout << "Black is the mode (most used)[" << mode << "] times" << endl;
					fout << "Black is the mode (most used)[" << mode << "] times" << endl;
					break;
			}
		}
	}

	fout << "Yellow ball (discount of 1 %) pulled " << tally_array[0] << " times" << endl;
	fout << "Blue ball (discount of 2 %) pulled " << tally_array[1] << " times" << endl;
	fout << "Red ball (discount of 3 %) pulled " << tally_array[2] << " times" << endl;
	fout << "Purple ball (discount of 4 %) pulled " << tally_array[3] << " times" << endl;
	fout << "Orange ball (discount of 5 %) pulled " << tally_array[4] << " times" << endl;
	fout << "Green ball (discount of 6 %) pulled " << tally_array[5] << " times" << endl;
	fout << "Maroon ball (discount of 7%) pulled " << tally_array[6] << " times" << endl;
	fout << "Black ball (discount of 8 %) pulled " << tally_array[7] << " times" << endl;
	fout << "Average (mean) is = " << mean << endl;


	cout << "Yellow ball (discount of 1 %) pulled " << tally_array[0] << " times" << endl;
	cout << "Blue ball (discount of 2 %) pulled " << tally_array[1] << " times" << endl;
	cout << "Red ball (discount of 3 %) pulled " << tally_array[2] << " times" << endl;
	cout << "Purple ball (discount of 4 %) pulled " << tally_array[3] << " times" << endl;
	cout << "Orange ball (discount of 5 %) pulled " << tally_array[4] << " times" << endl;
	cout << "Green ball (discount of 6 %) pulled " << tally_array[5] << " times" << endl;
	cout << "Maroon ball (discount of 7 %) pulled " << tally_array[6] << " times" << endl;
	cout << "Black ball (discount of 8 %) pulled " << tally_array[7] << " times" << endl;
	cout << "Average (mean) is = " << mean << endl;


	fout.close();
}
