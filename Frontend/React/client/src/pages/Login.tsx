const Login = () => {
	return (
		<div className="flex flex-col h-full">
			<nav className="w-full bg-green-500 py-10">
				<div className="flex max-w-6xl mx-auto">
					<h1 className="text-xl text-white font-semibold">
						Federal University of Technology Owerri
					</h1>
				</div>
			</nav>
			<main className="w-full h-full flex justify-center items-center">
				<form className="w-1/2 bg-white text-zinc-700 rounded-md shadow-xl p-10 flex flex-col gap-4">
					<input
						type="text"
						placeholder="Username"
						className="bg-zinc-100 w-full p-4 rounded"
					/>
					<input
						type="text"
						placeholder="Password"
						className="bg-zinc-100 w-full p-4 rounded"
					/>
					<button
						type="submit"
						className="bg-green-600 text-white w-full p-4 rounded"
					>
						Login
					</button>

                    <p></p>
				</form>
			</main>
		</div>
	);
};

export default Login;
