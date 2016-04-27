#include <iostream>
#include <string>
#include "LPD8806.hpp"

const uint16_t numLEDs = 36;
LPD8806 strip(numLEDs);
uint8_t r;
uint8_t g;
uint8_t b;
const uint16_t delay_const = 20;

void setPixels(uint16_t numLEDs, uint8_t r, uint8_t g, uint8_t b) {
  for(int i=0; i<numLEDs; i++){
    strip.setPixelColor(i,r,g,b);
  }
  strip.show();
}

void blue2red() {
  r = 0;
  g = 0;
  b = 125;
  while(b > 0) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    b--;
  }
  b = 0;
  setPixels(numLEDs, r, g, b);

  while(r < 125) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    r++;
  }
  r = 125;
  setPixels(numLEDs, r, g, b);
}

void red2blue() {
  r = 125;
  g = 0;
  b = 0;
  while(r > 0) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    r--;
  }
  r = 0;
  setPixels(numLEDs, r, g, b);

  while(b < 125) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    b++;
  }
  b = 125;
  setPixels(numLEDs, r, g, b);
}

void blue2white() {
  r = 0;
  g = 0;
  b = 125;
  while(b > 0) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    b--;
  }
  b = 0;
  setPixels(numLEDs, r, g, b);

  while(r < 125) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    r++;
    g++;
    b++;
  }
  r = 125;
  g = 125;
  b = 125;
  setPixels(numLEDs, r, g, b);
}

void red2white() {
  r = 125;
  g = 0;
  b = 0;
  while(r > 0) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    r--;
  }
  r = 0;
  setPixels(numLEDs, r, g, b);

  while(r < 125) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    r++;
    g++;
    b++;
  }
  r = 125;
  g = 125;
  b = 125;
  setPixels(numLEDs, r, g, b);
}

void white2blue() {
  r = 125;
  g = 125;
  b = 125;
  while(r > 0) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    r--;
    g--;
    b--;
  }
  r = 0;
  g = 0;
  b = 0;
  setPixels(numLEDs, r, g, b);

  while(b < 125) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    b++;
  }
  b = 125;
  setPixels(numLEDs, r, g, b);
}

void white2red() {
  r = 125;
  g = 125;
  b = 125;
  while(r > 0) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    r--;
    g--;
    b--;
  }
  r = 0;
  g = 0;
  b = 0;
  setPixels(numLEDs, r, g, b);

  while(r < 125) {
    setPixels(numLEDs, r, g, b);
    delay(delay_const);
    r++;
  }
  r = 125;
  setPixels(numLEDs, r, g, b);
}


void turnOff() {
  r = 0;
  g = 0;
  b = 0;
 
  setPixels(numLEDs, r, g, b);
}

void printUsage() {
  using namespace std;
  cout << "Usage: transitionLEDs <func_name>\n"
       << "Functions:\n"
       << "  blue2red\n"
       << "  red2blue\n"
       << "  blue2white\n"
       << "  red2white\n"
       << "  white2blue\n"
       << "  white2red\n";

}

int main(int argc, char** argv) {
  if (argc != 2) {
    printUsage();
  } else {
    std::string input = argv[1];
    std::string str1 = "blue2red";
    std::string str2 = "red2blue";
    std::string str3 = "blue2white";
    std::string str4 = "red2white";
    std::string str5 = "white2blue";
    std::string str6 = "white2red";
    std::string str7 = "turnoff";

    if (input.compare(str1) == 0) {
      blue2red();
    } else if (input.compare(str2) == 0) {    
      red2blue();
    } else if (input.compare(str3) == 0) {    
      blue2white();
    } else if (input.compare(str4) == 0) {    
      red2white();
    } else if (input.compare(str5) == 0) {    
      white2blue();
    } else if (input.compare(str6) == 0) {    
      white2red();
    } else if (input.compare(str7) == 0) {    
      turnOff();
    } else {
      printUsage();
    }

  return 0;
  }
}
