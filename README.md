# Crypto Trading Game

This project is a web-based cryptocurrency trading simulation game. Players can buy and sell various virtual coins in a simulated market to grow their portfolio.

## Gameplay

*   **Dynamic Market:** The game features a variety of coins with fluctuating prices. For example, a coin like "Lance Coin" might have its price programmed to increase to a certain point (e.g., $3) and then drop to a lower value (e.g., $1.50), creating trading opportunities.
*   **Trading:** Players can buy and sell coins. The interface shows the current price, the number of shares owned, the average cost of shares, and the price before the market opens.
*   **Commissions:** A commission is charged for each share traded, adding a realistic element to the game.
*   **Portfolio:** Players can track their performance through their portfolio, which displays the total value of their assets.

## Technology Stack

The application is built with a Django backend and a React frontend.

### Backend

The backend is a Django application that manages:
*   Game logic, including price fluctuations for different coins.
*   User accounts and their portfolios.
*   Trading transactions.

The backend consists of the following Django apps:
*   `common`: Common utilities.
*   `market`: Manages market data and coin information.
*   `trading`: Handles buying and selling operations.
*   `users`: Manages user accounts.

### Frontend

The frontend is a React application that provides the user interface for the game. Players interact with the market, view their portfolio, and make trades through the web interface.
