#pragma once
#include <string>

using FString = std::string;
using int32 = int;


struct FBullCowCount {
	int32 Bulls = 0;
	int32 Cows = 0;
};


enum EGuessStatus {
	Invalid_Status,
	OK,
	Not_Isogram,
	Wrong_Length,
	Has_Caps
};



class FBullCowGame {
public:

	FBullCowGame(); //constructor

	int32 GetMaxTries() const;
	int32 GetCurrentTry() const;
	int32 GetHiddenWordLength() const;
	EGuessStatus CheckGuessValidity(FString Guess) const;
	bool IsGameWon() const;
	bool IsLowerCase(FString Word) const;

	void Reset(); //TODO make a more rich method
	//counts bulls and cows and increase try # assuming a valid guess
	FBullCowCount SubmitValidGuess(FString Guess);

private:
	//init in constructor
	int32 MyCurrentTry;
	FString MyHiddenWord;
	bool bGameIsWon;

	bool IsIsogram(FString Word) const;
};
