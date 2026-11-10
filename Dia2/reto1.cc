#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>


int main(int argc, char* argv[]) {
  std::ifstream file(argv[1]);
  std::string linea;
  int contador = 0;

  while (std::getline(file, linea)) {
    std::istringstream iss(linea);
    std::vector<int> columna;
    int valor;
    while(iss >> valor) {
      columna.push_back(valor);
    }
    int anterior = columna[0];
    for(int i = 0; i < columna.size(); i++) {
      if(columna[i] > anterior) {
        break;
      }
      if(i == columna.size() - 1) {
        contador++;
      }
      anterior = columna[i];
    }
  }

  std::cout << contador << std::endl;

}