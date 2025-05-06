const [num1, num2] = [200, 123];

if (num1 < num2) {
	console.log(`Sure ${num1} is less than ${num2}`);
} else if (num1 === num2) {
	console.log(`Sure ${num1} is equal to ${num2}`);
} else {
	console.log(`${num1} is greater than ${num2}`);
}

const sentence = `This is some random sentence I have just written.
It is in the JS file.
`;

const sentence2 =
	'This is some random sentence I have just written.\nIt is in the JS file.';

if (sentence.includes('have')) {
	console.log("The word 'have' is in the sentence");
}

if (!sentence.includes('monumental')) {
	console.log("The word 'monumental' is not in the sentence");
}

if (sentence.length > 10) {
	console.log("This is a very long sentence!!");
}

if (sentence.length > 1000 || sentence.length > 10) {
	console.log('This is a veeeeery long sentence!!');
}