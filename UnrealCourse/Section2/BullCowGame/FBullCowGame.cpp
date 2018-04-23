#pragma once
#include "FBullCowGame.h"
#include <map>
#define TMap std::map

using int32 = int;

//Constructor
FBullCowGame::FBullCowGame() { Reset(); }

//Getter methods

int32 FBullCowGame::GetCurrentTry() const { return MyCurrentTry; }
int32 FBullCowGame::GetHiddenWordLength() const { return MyHiddenWord.length(); }
bool FBullCowGame::IsGameWon() const { return bGameIsWon; }


int32 FBullCowGame::GetMaxTries() const { 
	
	TMap <int32, int32> WordLengthToMaxTries{ {3,5}, {4,5}, {5,5}, {6,6} };
	return WordLengthToMaxTries[MyHiddenWord.length()];
}

bool FBullCowGame::IsLowerCase(FString Word) const {

	//handle edge cases like zero length and \0
	if (Word.length() == 0) { return false; }
	//go through all chars in Word
	for (auto Letter : Word) {
		if (!islower(Letter)) { return false; } //if char is not lowercase, return false
	}
	
	return true; //after loop, return true since no chars were uppercase
}

bool FBullCowGame::IsIsogram(FString Word) const { 
	
	//consider 0 and 1 letter words as isograms
	if (Word.length() <= 1) { return true; }

	//Create map for chars in word
	TMap <char, bool> LetterSeen;

	//loop through all letters of guessed word
	for (auto Letter : Word) { //for all letters of the Word
		Letter = tolower(Letter); //ignore case

		if (LetterSeen[Letter] == true) { //TMap values initialize to false so true means letter is duplicate
			return false; 
		}
		LetterSeen[Letter] = true;

	}
	return true; //for edge cases like \0 (end of string)

}

void FBullCowGame::Reset() {
		
	const FString HIDDEN_WORD = "planet";
	MyHiddenWord = HIDDEN_WORD;

	MyCurrentTry = 1;
	bGameIsWon = false;

	return;
}

EGuessStatus FBullCowGame::CheckGuessValidity (FString Guess) const {
	
	if (!IsIsogram(Guess)) { //if guess not isogram
		return EGuessStatus::Not_Isogram;
	}
	else if (!IsLowerCase(Guess)) { //if guess has capitals
		return EGuessStatus::Has_Caps;
	}
	else if (GetHiddenWordLength() != Guess.length()) { //if guess length is wrong
		return EGuessStatus::Wrong_Length;
	}
	else { 
		return EGuessStatus::OK; 
	}

	return EGuessStatus::OK; 
}

//Receives a valid guess, increments try number, returns count
FBullCowCount FBullCowGame::SubmitValidGuess(FString Guess) {

	MyCurrentTry++;
	FBullCowCount BullCowCount;
	int32 WordLength = GetHiddenWordLength(); //assuming hidden word and guess word are same length

	//loop through all letters of the hidden word
	for (int32 HidWordChar = 0; HidWordChar < WordLength; HidWordChar++) {

		//compare all letters of guess against the hidden word char
		for (int32 GuessChar = 0; GuessChar < WordLength; GuessChar++) {

			//if the letters AND positions of letters match, increment bulls
			if (MyHiddenWord[HidWordChar] == Guess[GuessChar] && HidWordChar == GuessChar) {
				BullCowCount.Bulls++;
				if (BullCowCount.Bulls == WordLength) {
					bGameIsWon = true;
				}
				break;
			}
			//if only the letters match (in different positions) then increment cows
			else if(MyHiddenWord[HidWordChar] == Guess[GuessChar]){
				BullCowCount.Cows++;
				break;
			}
		}
	}	
	return BullCowCount;
}
