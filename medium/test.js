let old =  [
  {
    volume: '0.01',
    symbol: 'EURUSD',
    type: 'BUY',
    duration: '\n                  02s\n                ',
    open_time: '\n                  12:22\n                '
  },
  {
    volume: '0.01',
    symbol: 'EURUSD',
    type: 'BUY',
    duration: '\n                  10s\n                ',
    open_time: '\n                  12:22\n                '
  },
  {
    volume: '0.01',
    symbol: 'EURUSD',
    type: 'BUY',
    duration: '\n                  49s\n                ',
    open_time: '\n                  12:22\n                '
  }
]

let newData =  [
  {
    volume: '0.01',
    symbol: 'EURUSD',
    type: 'BUY',
    duration: '01m 20s',
    open_time: '12:22'
  },
  {
    volume: '0.01',
    symbol: 'EURUSD',
    type: 'BUY',
    duration: '01m 28s',
    open_time: '12:22'
  }
];

function compare(old, newData) {
	const diff = [];
	const newData_copy = [...newData];
	console.log(newData_copy);
	for (let x of old){
		var isIn = null;
		for (let y = 0; y < newData_copy.length; y++){
			if (newData_copy[y] != undefined){
				console.log(`${x.open_time.trim()} === ${newData_copy[y].open_time.trim()}`, x.open_time.trim() === newData_copy[y].open_time.trim());
				console.log(`${x.volume} === ${newData_copy[y].volume}`, x.volume === newData_copy[y].volume);
				console.log(`${x.symbol} === ${newData_copy[y].symbol}`, x.symbol === newData_copy[y].symbol);
				console.log(`${x.type} === ${newData_copy[y].type}`,  x.type === newData_copy[y].type);
              // trim cause the issue to remove
				if (x.open_time.trim() === newData_copy[y].open_time.trim() && x.volume === newData_copy[y].volume && x.symbol === newData_copy[y].symbol && x.type === newData_copy[y].type){
					isIn = 1;
					delete newData_copy[y];
					break;
				}
			}
		}
		if (isIn == null){
			diff.push(x)
		}
	}
	return diff;

}

console.log(compare(old, newData));
