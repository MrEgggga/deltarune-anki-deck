all: src/lines.json deck/data.txt

src/lines.json:
	pushd src
	node generate.js
	popd

deck/data.txt:
	src/ankify.py > deck/data.txt

clean:
	rm src/lines.json deck/data.txt