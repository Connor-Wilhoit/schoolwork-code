#include <iostream>
#include <vector>
#include <algorithm>
//cout << "Max Element = " << *max_element(scores.begin(), scores.end()) << endl;
using namespace std;

int main()
{
	vector<int> scores;
	vector<int> histogram;
	int * max = new int;
	int * temp = new int;
	int grade=0;

	cout << "Enter: the student's scores, terminating with -1:\n";
	while(grade != -1)
	{
		cin >> grade;
		scores.push_back(grade);
	}
	
	*max = *max_element(scores.begin(), scores.end());
	sort(scores.begin(), scores.end());
	for(int i=1; i < scores.size(); i++)
	{
		*temp = scores[i];
		int mycount = count(scores.begin(), scores.end(), *temp);
		cout << "Number of " << *temp << "'s: " << mycount << endl;
		for(int j=1; j < scores.size(); j++)
		{
			if(*temp == scores[j])
			{
				scores.erase(scores.begin()+j);

			}
		}
	}
	return 0;
}
