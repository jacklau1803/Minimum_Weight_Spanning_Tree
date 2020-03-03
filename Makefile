# This is a fake makefile to comply with the grading procedure.
# All it does is make a copy of my Python3 program and name it without the file extension and chmod +x it.
# And make clean deletes it.
SOURCES=MWST.py
TARGET=MWST

all: copy

clean:
	-rm $(TARGET)

copy:
	cp $(SOURCES) $(TARGET)
	chmod +x $(TARGET)