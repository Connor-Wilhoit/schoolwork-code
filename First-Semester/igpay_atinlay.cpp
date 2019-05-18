#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
	string first, last, new_str;

	cout << "Enter your first name: ";
	getline(cin, first);
	cout << "Enter your last name: ";
	getline(cin, last);

	for(unsigned i=0; i < first.length(); i++)
	{
		if(isupper(first.at(i)))
		{
			first.at(i) = tolower(first.at(i));
		}
	}
	for(unsigned i=0; i < last.length(); i++)
	{
		if(isupper(last[i]))
		{
			last[i] = tolower(last[i]);
		}
	}
	for(int i=0; i < 1; i++)
	{
		if((first.at(i) == 'a') || (first.at(i) == 'e') ||
			(first.at(i) == 'i') || (first.at(i) == 'o') ||
			(first.at(i) == 'u'))
		{
			first.append("way");
		}
		else
		{
			char c = first.at(i);
			first.erase(first.begin());
			first.push_back(c);
			first.append("ay");
		}
	}
	for(int i=0; i < 1; i++)
	{
		if((last.at(i) == 'a') || (last.at(i) == 'e') ||
			(last.at(i) == 'i') || (last.at(i) == 'o') ||
			(last.at(i) == 'u'))
		{
			last.append("way");
		}
		else
		{
			char c = last.at(i);
			last.erase(last.begin());
			last.push_back(c);
			last.append("ay");
		}

	}

	first.at(0) = toupper(first.at(0));
	last.at(0) = toupper(last.at(0));
	new_str = first + " " + last;
	cout << new_str << endl;


	return 0;
}
