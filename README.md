# cli-currency-watcher-coinmarket
Here's a simple Python CLI tool written using Click. It allows you to get the current value of a crypto-currency via it's full name (example : safe-exchange-coin for SAFEX) . 

Requires python 3.6+

## Installation 

`git clone git@github.com:sorasful/cli-currency-watcher-coinmarket.git`  
then cd into the cloned directory  

`pip install -r requirements.txt`  

If you want to use it using the UNIX syntax :   

`chmod a+x currency_watcher`


## Usage

No argument (get Bitcoin currency)  
`python currency_watcher`

With argument :  
`python currency_watcher -c nexus`

or directly using 

`./currency_watcher -c nexus`
