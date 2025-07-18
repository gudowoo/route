# RouterNg

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 8.1.0.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

## Python trading example

A simple trading script is available in `auto_trader.py`. It uses `yfinance` to
retrieve market data and `alpaca_trade_api` to place orders. Set the following
environment variables before running:

```
export ALPACA_API_KEY=<your key>
export ALPACA_SECRET_KEY=<your secret>
export TRADE_SYMBOL=AAPL  # or any stock symbol
```

Execute the script with:

```
python auto_trader.py
```

The example implements a basic moving average strategy and submits market orders
through the Alpaca API.
