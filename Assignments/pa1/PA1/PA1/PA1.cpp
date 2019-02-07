#include "PA1.h"

/// <summary>
/// Helper to make a huffman tree.
/// Maps the character frequency.
///Outputs a hash table with the frequency of characters in the data.
/// </summary>
/// <param name="data">Vector of strings, which needs its frequency of characters within all strings mapped</param>
/// <returns>Returns a hashTable with a int frequency of each character</returns>
unordered_map<char, int> mapCharFrequency(const vector<string> data)
{
    unordered_map<char, int> freqMap;

    for (auto str : data)
    {
        for (auto ch : str)
        {
            if (freqMap.find(ch) != freqMap.end())
            {
                //If character already exists increment the frequency of the character.
                freqMap[ch]++;
            }
            else
            {
                //Else insert into map with a value of 1.
                freqMap[ch] = 1;
            }
        }

    }

    return freqMap;
}

/// <summary>
/// Builds a huffmans tree from a vector of strings.
/// </summary>
/// <param name="data">Vector of strings, which needs its frequency of characters within all strings mapped</param>
/// <returns>Returns a huffman tree with frequencies of each character in data.</returns>
HuffmanTree<char>* PA1::huffmanTreeFromText(vector<string> data)
{
    //Create data frequency map.
    unordered_map<char, int> dataFreqMap = mapCharFrequency(data);

    //maintains huffman tree forest 
    priority_queue < HuffmanTree<char>*, vector<HuffmanTree<char>*>, TreeComparer> forest{};

    for (auto kvp : dataFreqMap)
    {
        forest.push(new HuffmanTree<char>(kvp.first, kvp.second));
    }

    while (forest.size() >= 2)
    {
        //Get smallest and make it left child.
        HuffmanTree<char> *leftChild = forest.top();
        forest.pop();
        
        //Get next smallest and make it right child.
        HuffmanTree<char> *rightChild = forest.top();
        forest.pop();

        //Merge the trees.
        HuffmanTree<char> *node = new HuffmanTree<char>(leftChild, rightChild);
        forest.push(node);

    }


    //At this point only 1 tree should remain so we get it and return.
    return forest.top();
}

/// <summary>
/// Edits a huffman tree provided from calling function.
/// Adds characters at the locations symbolized by the binPathStr
/// </summary>
/// <param name="tree">A huffman tree node.</param>
/// <param name="ch">The character to insert into tree.</param>
/// <param name="binPathStr">The binary path for the character.</param>
void huffmanTreeFromMapHelper(HuffmanTree<char> *tree, char ch, string binPathStr)
{
    //Base case.
    if (binPathStr.size() < 1)
    {
        return;
    }

    if (tree == nullptr)
    {
        //If tree doesn't exist create it.
        tree = new HuffmanTree<char>(new HuffmanInternalNode<char>(nullptr, nullptr));
    }

    //Pointers to keep track of where we are.
    HuffmanNode<char> *previous = tree->getRoot();
    HuffmanNode<char> *current = previous;

    for (auto c : binPathStr)
    {
        //0 means go left, 1 means go right.
        if (c == '0')
        {
            current = current->getLeftChild();

            if (current == nullptr && c == binPathStr[binPathStr.size() - 1])
            {
                //If we are at the end and the leaf doesn't exist, create it.
                current = new HuffmanLeafNode<char>(ch, 0);
                previous->setLeftChild(current);
                return;
            }
            else if (current == nullptr)
            {
                //If we aren't at the end and the node doesn't exist, create an internal node.
                current = new HuffmanInternalNode<char>(nullptr, nullptr);
                previous->setLeftChild(current);
            }

            previous = current;

        }
        else if (c == '1')
        {
            current = current->getRightChild();

            if (current == nullptr && c == binPathStr[binPathStr.size() - 1])
            {
                //If we are at the end and the leaf doesn't exist, create it.
                current = new HuffmanLeafNode<char>(ch, 0);
                previous->setRightChild(current);
                return;
            }
            else if (current == nullptr)
            {
                //If we aren't at the end and the node doesn't exist, create an internal node.
                current = new HuffmanInternalNode<char>(nullptr, nullptr);
                previous->setRightChild(current);
            }

            previous = current;
        }
    }
}

/// <summary>
/// Creates a huffman tree from a huffman map.
/// </summary>
/// <param name="huffmanMap">huffman map.</param>
/// <returns>Returns a huffman tree created from the map given.</returns>
HuffmanTree<char>* PA1::huffmanTreeFromMap(unordered_map<char, string> huffmanMap)
{
    //Base case.
    if (huffmanMap.empty())
    {
        return nullptr;
    }

    //Create a new tree.
    HuffmanTree<char> *tree = new HuffmanTree<char>(new HuffmanInternalNode<char>(nullptr, nullptr));

    for (auto kvp : huffmanMap)
    {
        //Pass tree and each kvp to the helper function, which will add the kvp to the tree.
        huffmanTreeFromMapHelper(tree, kvp.first, kvp.second);
    }

    return tree;
}

/// <summary>
/// Helper function to make an encoding map from a huffman tree.
/// </summary>
/// <param name="map">The encoding map to change.</param>
/// <param name="node">A node of the huffman tree.</param>
/// <param name="encoding">The current encoding string path.</param>
void huffmanEncodingMapFromTreeHelper(unordered_map<char, string>& map, HuffmanNode<char>* node, string encoding)
{
    if (node->isLeaf() == false)
    {
        //If not a leaf make recursive calls.
        huffmanEncodingMapFromTreeHelper(map, node->getLeftChild(), encoding += '0');
        huffmanEncodingMapFromTreeHelper(map, node->getRightChild(), encoding  += '1');
        return;
    }
    else
    {
        //Else we have a complete mapping for character.
        map[node->getValue()] = encoding;
        return;
    }
}

/// <summary>
/// Creates and returns a encoding map from a huffman tree.
/// </summary>
/// <param name="tree">A huffman tree.</param>
/// <returns>Returns an encoding map of characters in the tree.</returns>
unordered_map<char, string> PA1::huffmanEncodingMapFromTree(HuffmanTree<char> *tree)
{
    unordered_map<char, string> result{};
    huffmanEncodingMapFromTreeHelper(result, tree->getRoot(), "");
    return result;
}

/// <summary>
/// Writes an encoding map to the filename provided.
/// Writes it as single line per kvp like "A001".
/// Where A is the char, and 001 is the encoding.
/// </summary>
/// <param name="huffmanMap">Ahuffman map.</param>
/// <param name="file_name">Name of the file to write to.</param>
void PA1::writeEncodingMapToFile(unordered_map<char, string> huffmanMap, string file_name)
{
    //If empty, nothing to write so return.
    if (huffmanMap.empty())
    {
        return;
    }

    ofstream outputFile{ file_name };

    if (outputFile.good())
    {
        for (auto kvp : huffmanMap)
        {
            outputFile << kvp.first << kvp.second << endl;
        }
    }
    else
    {
        cout << "Error creating output file.";
        return;
    }
}

/// <summary>
/// Reads an huffman encoding file and puts it into an encoding map.
/// </summary>
/// <param name="file_name">Name of the file.</param>
/// <returns>Returns an huffman encoding map.</returns>
unordered_map<char, string> PA1::readEncodingMapFromFile(string file_name)
{
    //Creates a Huffman Map from the supplied file.
    //this is the inverse of writeEncodingMapToFile.
    ifstream inputFile{ file_name };
    unordered_map<char, string> encodingMap{};

    if (inputFile.good())
    {
        string currentLine;

        while (inputFile.good())
        {
            getline(inputFile, currentLine);

            //Input encoding into encoding map,
            //First character is the character that's encoded.
            //The rest is the encoding to that character.
            if (currentLine.size() > 1)
            {
                encodingMap[currentLine[0]] = currentLine.substr(1, currentLine.size() - 1);
            }
        }
    }
    else
    {
        cout << "Error opening input file";
        return encodingMap;
    }

    return encodingMap;
}


string decodeBitsHelper(HuffmanNode<char>* const root, vector<bool> bits)
{
    //Base cases.
    if (root == nullptr)
    {
        return "";
    }
    else if (bits.size() < 1)
    {
        return "";
    }

    string decodedString;
    HuffmanNode<char>* current = root;

    for (auto bit : bits)
    {
        if (bit == false)
        {
            //If false go left.
            current = current->getLeftChild();
        }
        else
        {
            //Else go right.
            current = current->getRightChild();
        }

        if (current->isLeaf())
        {
            //If leaf add value to decoded string and restart at root.
            decodedString += current->getValue();
            current = root;
        }
    }
    
    return decodedString;
}

//PA #1 TODO: Converts a vector of bits (bool) back into readable text using the supplied Huffman map
string PA1::decodeBits(vector<bool> bits, unordered_map<char, string> huffmanMap)
{
    //Create tree from map.
    HuffmanTree<char>* tree = huffmanTreeFromMap(huffmanMap);
    ostringstream result{};

    result << decodeBitsHelper(tree->getRoot(), bits);

    return result.str();
}

/// <summary>
/// Compresses text based on the huffman map to a vector of bools.
/// True is 1, false is 0.
/// </summary>
/// <param name="text">The text.</param>
/// <param name="huffmanMap">The huffman map.</param>
/// <returns></returns>
vector<bool> PA1::toBinary(vector<string> text, unordered_map<char, string> huffmanMap)
{
    vector<bool> result{};

    if (text.size() > 1 && huffmanMap.size() > 1)
    {
        for (auto str : text)
        {
            for (auto ch : str)
            {
                //Get value for character.
                string value = huffmanMap[ch];

                for (auto binStr : value)
                {
                    if (binStr = '0')
                    {
                        result.push_back(false);
                    }
                    else
                    {
                        result.push_back(true);
                    }
                }
            }
        }
    }
    
    return result;
}