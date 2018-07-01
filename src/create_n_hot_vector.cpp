#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>

int main(int argc, char** argv)
{
  using namespace std;
  if (argc < 2) {
    cerr << "I need header file for vector\n";
    return EXIT_FAILURE;
  }

  const auto human_vector_template {[ifs = ifstream{argv[1]}]() mutable {
    map<string, bool> human_headers {};
    for (string s; ifs >> s;)
      human_headers.emplace(s, false);
    return human_headers;
  }()};

  cout << "year";
  for (const auto& e : human_vector_template)
    cout << ',' << e.first;
  cout << '\n';

  for (string line; getline(cin, line);) {
    istringstream iss {line};
    {
      string date {};
      getline(iss, date, ',');
      cout << date;
    }
    
    auto human_vector {human_vector_template};
    for (string name; getline(iss, name, ',');)
      human_vector[name] = true;

    for (const auto& e : human_vector)
      cout << ',' << e.second;
    cout << '\n';
  }
}
