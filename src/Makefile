LIBDIR = $(DESTDIR)/usr/lib/python2.7/dist-packages/

clean:
	rm -f *.py[co] */*.py[co]

install:
	mkdir -p $(LIBDIR)/PyRfid
	cp -r PyRfid $(LIBDIR)/

uninstall:
	rm -rf $(LIBDIR)/PyRfid/
