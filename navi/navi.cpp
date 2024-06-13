#include<iostream>
#include<string>
#include<stdlib.h>
#include<thread>
#include<vector>

#ifdef _WIN32
#include<windows.h>
#else
#include<unistd.h>
#endif

using namespace std;

vector<string> texts = {
	"Welcome Back!",
	"\033[0;34m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
	"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
	"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
	"⠀⠀⠀⠀⢀⣤⣾⣿⠀⣠⣾⣿⡿⠛⠛⠛⠛⠿⣿⣷⣤⠀⣿⣷⣤⡀⠀⠀⠀⠀",
	"⠀⠀⢀⣴⣿⠿⠋⠀⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⠀⠙⠻⣿⣦⡀⠀⠀",
	"⠀⣰⣿⡟⠁⠀⠀⣸⣿⡏⠀⠀⢠⣾⣿⣿⣷⣄⠀⠀⢹⣿⣧⠀⠀⠈⢻⣿⣦⠀",
	"⠐⣿⣿⡀⠀⠀⠀⣿⣿⡇⠀⠀⢻⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠀⢀⣿⣿⠇",
	"⠀⠙⢿⣷⣄⡀⠀⠸⣿⣷⡀⠀⠈⠛⠿⠿⠛⠁⠀⢀⣾⣿⠇⠀⠀⣠⣾⡿⠋⠀",
	"⠀⠀⢀⡙⢿⣿⣦⣄⠹⣿⣿⣦⡀⠀⠀⠀⠀⢀⣤⣾⣿⠏⣠⣴⣿⡿⢋⡀⠀⠀",
	"⠀⠀⠿⠟⠀⠈⠛⠛⠀⠈⠛⠿⣿⣷⠀⠀⣾⣿⠿⠛⠁⠀⠛⠛⠁⠀⠻⠿⠀⠀",
	"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
	"⠀⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⣽⣿⠀⠀⣿⣿⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀",
	"⠀⠀⠀⠀⠀⠀⠙⢿⣷⣦⣤⣴⣿⠟⠀⠀⠻⣿⣦⣤⣴⣾⡿⠋⠀⠀⠀⠀⠀⠀",
	"⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀",
	"",
	"NaviOs 1.0.5-savari\033[0m",
	"Copyright 1991 (c) Copland OS Enterprise",
	"Produced by Tachibana Lab"
};

void println_view(const string& text, int delay_ns = 500*1000*1000, int s_left = 0) {
	int a = 0;
	for (a; a < s_left; a++) {
		cout << " ";
	}
	for (size_t i = 0; i < text.length(); ++i) {
		char subtext = text[i];
		cout << subtext << flush;
#ifdef _WIN32
		this_thread::sleep_for(chrono::milliseconds(delay_ns / 1000 * 1000));
#else
		this_thread::sleep_for(chrono::nanoseconds(delay_ns));
#endif
	}
	cout << endl;
}

void cls() {
#ifdef _WIN32
	system("cls");
#else
	system("clear");
#endif
}

int main() {
	cls();
	cout << endl;
	for (const auto& text : texts) {
		println_view(text, 300*1000, 2);
	}
	return 0;
}
