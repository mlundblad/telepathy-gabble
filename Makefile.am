ACLOCAL_AMFLAGS = -I m4

SUBDIRS = docs tools extensions lib src data m4 plugins tests gabble

DISTCHECK_CONFIGURE_FLAGS = --disable-debug --enable-gtk-doc

CLEANFILES = FIXME.out

check-twisted: all
	$(MAKE) -C tests/twisted check-twisted

check-all: check check-twisted

check-local::
	egrep -A 5 '[F]IXME|[T]ODO|[X]XX' $(srcdir)/src/*.[ch] \
		> FIXME.out || true

include tools/lcov.am
LCOV_CHECK_ARGS = CHECK_TWISTED_SLEEP=6

CHANGELOG_RANGE = telepathy-gabble-0.12.0..
CHECK_FOR_UNRELEASED = \
	$(srcdir)/NEWS \
	$(wildcard $(srcdir)/gabble/*.[ch]) \
	$(wildcard $(srcdir)/src/*.[ch])

include tools/telepathy.am
