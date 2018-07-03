#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main(int argc, char** argv)
{
  using namespace std;
  if (argc < 2) {
    cerr << "I need header file for vector\n";
    return EXIT_FAILURE;
  }

  const auto domain_vector {[ifs = ifstream{argv[1]}]() mutable {
    vector<string> domain_headers {};
    for (string s; ifs >> s;)
      domain_headers.emplace_back(s);
    return domain_headers;
  }()};

  for (string line; getline(cin, line);) {
    istringstream iss {line};
    string target;
    getline(iss, target, ',');
    cout << distance(domain_vector.begin(), find(domain_vector.begin(), domain_vector.end(), target)) << ',' << iss.rdbuf() << '\n';
  }
}
