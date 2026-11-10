#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

int main(int argc, char* argv[]) {
  std::ifstream file(argv[1]);
  std::vector<int> columna1;
  std::vector<int> columna2;
  std::string linea;

  while (std::getline(file, linea)) {
    std::istringstream iss(linea);
    int valor1, valor2;
    iss >> valor1 >> valor2;
    columna1.push_back(valor1);
    columna2.push_back(valor2);
  }

  std::sort(columna1.begin(), columna1.end());
  std::sort(columna2.begin(), columna2.end());


  int sumador = 0;
  for(int i = 0; i < columna1.size(); i++) {
    sumador += std::abs(columna1[i] - columna2[i]);
  }

  std::cout << sumador << std::endl;
}