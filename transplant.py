#!/usr/bin/env python
import collections
import struct
import sys

Section = collections.namedtuple('Section', ['tag', 'checksum', 'offset', 'length'])

assert len(sys.argv) == 3, "Usage: transplant.py <donor_font> <recepient_font>"
donor = open(sys.argv[1], 'rb').read()
donor_num_sections = struct.unpack_from('>4xh', donor)[0]
print('Donor sections: {}'.format(donor_num_sections))

donor_sections_offset = 4+2+2+2+2
donor_tables = {}
for i in range(donor_num_sections):
	(tag, checksum, offset, length) = struct.unpack_from('>4slll', donor, offset=donor_sections_offset + i * (4+4+4+4))
	print(tag, length)
	donor_tables[tag] = Section(tag, checksum, offset, length)

donor_cmap_info = donor_tables[b'cmap']
donor_cmap_offset = donor_cmap_info.offset