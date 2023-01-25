// encrypt
n=6731
ed=37
chrs = "Hello World!"
// -
encDec = ""
for(let c of chrs.match( new RegExp(`.{1,1}`,"g")) ) {
	b = parseInt( BigInt( BigInt(c.charCodeAt(0)) ** BigInt(ed) ) % BigInt(n) )
	h = ""
	_h = b.toString(16)
	for(let i = 0; i< (4-_h.length); i++) h += "0"
	encDec += h + _h
}
encDec = btoa(encDec)

// decrpt
n=6731
ed=2125
chrs = "MGVlYjE3NDQwYWQ3MGFkNzEyNTkwZDZkMTMwOTEyNTkxMDNjMGFkNzEyZjMxNTVm"
// -
encDec = ""
try { chrs = atob(chrs) }
catch(e) {}
for(let c of chrs.match( new RegExp(`.{1,4}`,"g") ) ) {
	b = parseInt( BigInt( BigInt(parseInt(c, 16)) ** BigInt(ed) ) % BigInt(n) )
	encDec += String.fromCharCode(b)
}
