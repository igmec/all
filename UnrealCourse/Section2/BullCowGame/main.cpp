/*
This is the console executable that makes use of the BullCow class
This acts as the view in a MVC pattern, and is responsible for all
user interaction. For game logic, see FBullCowGame class.

*/

#pragma once
#include <iostream>
#include <string>
#include "FBullCowGame.h"

using FText = std::string;
using int32 = int;

void PrintIntro();
void PlayGame();
void PrintGameSummary();
FText GetValidGuess();
bool AskToPlayAgain();


FBullCowGame BCGame; //instantiate a new game

//Entry point for application
int main() {

	do {
		PrintIntro();
		//TODO select difficulty, create new method for it
		PlayGame();
	} while (AskToPlayAgain());
	
	std::cout << "Thanks for playing!\n";

	return 0;
}

void PlayGame(){
	
	BCGame.Reset(); //TODO pass in a difficulty level
	int32 MaxTries = BCGame.GetMaxTries();
	std::cout << MaxTries << std::endl;	

	//loop asking for guesses while game is NOT won and there are tries remaining
	while (!BCGame.IsGameWon() && BCGame.GetCurrentTry() <= MaxTries) {
		FText Guess = GetValidGuess();

		//Submit valid guess to game
		FBullCowCount BullCowCount = BCGame.SubmitValidGuess(Guess);

		std::cout << "Bulls = " << BullCowCount.Bulls;
		std::cout << ", Cows = " << BullCowCount.Cows << std::endl;
	}
	PrintGameSummary();

	return;
}


//Introduce the game
void PrintIntro() {
	
	std::cout << "Welcome to Bulls and Cows, a fun word game." << std::endl;
	std::cout << "Can you guess the " << BCGame.GetHiddenWordLength();
	std::cout << " letter isogram?\n";
	return;
}

//Get a guess from user and print it
FText GetValidGuess() {	

	FText Guess = "";
	EGuessStatus Status = EGuessStatus::Invalid_Status;

	do {
		int32 CurrentTry = BCGame.GetCurrentTry();
		std::cout << "\nTry " << CurrentTry << " of " << BCGame.GetMaxTries();
		std::cout << ". Enter your guess: ";
		std::getline(std::cin, Guess);

		Status = BCGame.CheckGuessValidity(Guess);
		switch (Status) {
		case EGuessStatus::Wrong_Length:
			std::cout << "Please enter a " << BCGame.GetHiddenWordLength() << " letter word.\n";
			break;

		case EGuessStatus::Not_Isogram:
			std::cout << "Please enter a word without repeating letters.\n";
			break;

		case EGuessStatus::Has_Caps:
			std::cout << "Please enter all lower case letters.\n";
			break;

		default:
			//assume guess is valid
			break;
		}
	} while (Status != EGuessStatus::OK); //loop until there are no errors
	
	return Guess;
}

void PrintGameSummary() {

	if (BCGame.IsGameWon()) std::cout << "Congrats! You guessed the word, you won!\n\n";
	else std::cout << "Looks like you couldn't guess the word. Try again.\n\n";
	return;
}

bool AskToPlayAgain(){

	std::cout << "Do you want to play again with the same word?(Y/N): ";
	FText Response = "";
	std::getline(std::cin, Response);
	std::cout << std::endl << std::endl;
	return (Response[0] == 'y' || Response[0] == 'Y');
}
