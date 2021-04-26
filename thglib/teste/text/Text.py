from thglib.teste.text.constantes import (
    Names_Female,
    Names_Male,
    Surnames,
    Iconv_ASCII,
    Iconv_EBCDIC,
    Iconv_ISO8859_1,
    Iconv_IBM1047,
    TLDs,
    States,
    UpperAlpha,
    LowerAlpha,
    Numerals,
    Base32,
    Base64,
    Base64Url,
    Alpha,
    AlphaNumeric,
    DefaultWrap,
    Punctuation,
)
import bz2
##
#
# Serialization
#
##

#
# Converts a raw string into a python buffer
#

def raw_string_into_a_python_buffer(str) -> bytes:
    return bz2.decompress(str.encode('raw_unicode_escape'))


#
# Creates a comma separated list of numbers
#
def create_separated_list_of_numbers(listt) -> list:
    return list(','.join([str(i) for i in listt]))


#
# Creates a comma separated list of dwords
#
#todo:Creates a comma separated list of dwords

#
# Creates a ruby-style comment
# Creates a javascript-style comment
# Creates a javascript-style comment
# add fist caracter on line
def creates_a_style_comment(filepath:str,mode="")->str:
    with open(filepath) as fp:
        lines = fp.read().splitlines()
    with open(filepath, "w") as fp:
        for line in lines:
            print(mode + line, file=fp)
a= creates_a_style_comment(filepath="a.py",mode="#")
"""

  #
  # Converts a raw string into a C buffer
  #
  def self.to_c(str, wrap = DefaultWrap, name = "buf")
    return hexify(str, wrap, '"', '"', "unsigned char #{name}[] = \n", '";')
  end

  def self.to_csharp(str, wrap = DefaultWrap, name = "buf")
    ret = "byte[] #{name} = new byte[#{str.length}] {"
    i = -1;
    while (i += 1) < str.length
      ret << "\n" if i%(wrap/4) == 0
      ret << "0x" << str[i].unpack("H*")[0] << ","
    end
    ret = ret[0..ret.length-2] #cut off last comma
    ret << " };\n"
  end

  #
  # Creates a c-style comment
  #
  def self.to_c_comment(str, wrap = DefaultWrap)
    return "/*\n" + wordwrap(str, 0, wrap, '', ' * ') + " */\n"
  end



  #
  # Converts a raw string into a perl buffer
  #
  def self.to_perl(str, wrap = DefaultWrap, name = "buf")
    return hexify(str, wrap, '"', '" .', "my $#{name} = \n", '";')
  end

  #
  # Converts a raw string into a python buffer
  #
  def self.to_python(str, wrap = DefaultWrap, name = "buf")
    return hexify(str, wrap, "#{name} += \"", '"', "#{name} =  \"\"\n", '"')
  end

  #
  # Converts a raw string into a Bash buffer
  #
  def self.to_bash(str, wrap = DefaultWrap, name = "buf")
    return hexify(str, wrap, '$\'', '\'\\', "export #{name}=\\\n", '\'')
  end

  #
  # Converts a raw string into a java byte array
  #
  def self.to_java(str, name = "shell")
    buff = "byte #{name}[] = new byte[]\n{\n"
    cnt = 0
    max = 0
    str.unpack('C*').each do |c|
      buff << ", " if max > 0
      buff << "\t" if max == 0
      buff << sprintf('(byte) 0x%.2x', c)
      max +=1
      cnt +=1

      if (max > 7)
        buff << ",\n" if cnt != str.length
        max = 0
      end
    end
    buff << "\n};\n"
    return buff
  end

  #
  # Converts a raw string to a powershell byte array
  #
  def self.to_powershell(str, name = "buf")
    return Rex::Powershell::Script.to_byte_array(str, name)
  end
"""
"""def create_separated_list_of_dword(text, wrap=DefaultWrap):
    code = text
    alignnr = len(text) % 4
    if (alignnr > 0):
        code == "\x00" * (4 - alignnr)
    codevalues = []
    while code.split(""),(4):
        chars4 = chars4.join("")
        dwordvalue = chars4.unpack('*V')
        codevalues.push(dwordvalue[0])
    buff = ""
    for i in range(codevalues.__len__() - 1):
        if (i % 8 == 0) and (buff.__len__() > 0):
            buff + "\r\n"

        buff + " " + print(f'0x{codevalues[i]}.8x, ')

    # strip , at the end
    buff = buff.split(', ')
    return buff << "\r\n"
a = create_separated_list_of_dword("dsa")
print(a)"""
