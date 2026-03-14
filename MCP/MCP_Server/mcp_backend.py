# arith_server.py
from __future__ import annotations
from fastmcp import FastMCP


# Create MCP server instance
mcp = FastMCP("arith")


def _as_number(x):
    """
    Accept ints, floats, or numeric strings.
    Raise a clean error otherwise.
    """
    if isinstance(x, (int, float)):
        return float(x)

    if isinstance(x, str):
        try:
            return float(x.strip())
        except ValueError:
            pass

    raise TypeError("Expected a number (int, float, or numeric string)")


@mcp.tool()
async def add(a: float, b: float) -> float:
    """Return a + b."""
    return _as_number(a) + _as_number(b)


@mcp.tool()
async def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return _as_number(a) - _as_number(b)


@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return _as_number(a) * _as_number(b)


@mcp.tool()
async def divide(a: float, b: float) -> float:
    """Return a / b."""
    denominator = _as_number(b)
    if denominator == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return _as_number(a) / denominator


@mcp.tool()
async def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return _as_number(a) ** _as_number(b)


@mcp.tool()
async def modulus(a: float, b: float) -> float:
    """Return a % b."""
    divisor = _as_number(b)
    if divisor == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed")
    return _as_number(a) % divisor


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
