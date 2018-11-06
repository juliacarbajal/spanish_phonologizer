BEGIN{RS="[\*\@\%\n]"}
/^ID/ {
isachild=tolower($0)~"(child)|(target-child)|(brother)|(sister)|(playmate)|(girl)|(boy)|(cousin)"
if ($3 == ",")
	n=split($4,a,"|");
else
	n=split($2,a,"|");
print isachild,FILENAME,a[3],a[1],"	" $0
}