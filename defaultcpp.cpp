#include <iostream>
#include <string>

//Const
const std::string NAME = "Testing"; // Name of the program

int fncExit()
{
	std::cout<<"Press any key to continue...";
	std::cin.get();
	std::cin.get();
	return 0;
}

int main()
{
	bool bExit = false; // Running flag
	std::cout<<"Welcome to " + NAME + "!\n";
	while (bExit != true)
	{
	}
	return fncExit();
}
