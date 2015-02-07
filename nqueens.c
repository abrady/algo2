#include <stdlib.h>
#include <string.h>

#define true 1
#define false 0

int nqueens_worker(char *board, int n, int queen);
int check_and_place(char *board, int row, int col);

int nqueens(int n) {
  // I don't make people write memory allocation code in interview
  char *board = (char*)malloc(n);
  memset(board, 0, n);
  int ret = nqueens_worker(board, n, 0);
  free(board);
  return ret;
}

#include "stdio.h"
int main(int ac, char **av) {
  int r = nqueens(8);
  printf("n queens: %d\n",r);
}

int nqueens_worker(char *board, int n, int queen) {
  if (queen == n) {
    return true;
  }

  for (int col = 0; col < n; ++col) {
    if (check_and_place(board, queen, col) && nqueens_worker(board, n, queen + 1)) {
      return true;
    }
  }

  return false;
}

// board:

int check_and_place(char *board, int row, int col) {
  // can't be any queens in or past row
  // also can't be any row conflicts since we only place 1 per row
  for (int i = 0; i < row; ++i) {
    if ((board[i] == col) || ((row - i) == abs(col - board[i]))) {
      return false;
    }
  }

  board[row] = col;
  return true;
}
