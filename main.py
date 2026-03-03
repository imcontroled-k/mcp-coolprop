from fastmcp import FastMCP
import CoolProp.CoolProp as CP

# MCP 서버 이름 설정
mcp = FastMCP("CoolProp-Engine")

@mcp.tool()
def get_fluid_property(fluid: str, output_key: str, prop1: str, val1: float, prop2: str, val2: float) -> str:
    """
    CoolProp을 사용하여 유체의 열역학 물성치를 계산합니다.
    예: fluid='Water', output_key='D'(밀도), prop1='T', val1=300, prop2='P', val2=101325
    """
    try:
        # SI 단위로 계산 (결과값: float)
        result = CP.PropsSI(output_key, prop1, val1, prop2, val2, fluid)
        return f"{fluid}의 {output_key} 값은 {result} [SI 단위] 입니다."
    except Exception as e:
        return f"계산 오류: {str(e)}"

@mcp.tool()
def list_fluids() -> list:
    """사용 가능한 유체 리스트의 일부를 반환합니다."""
    return ["Water", "R134a", "CO2", "Ammonia", "Air", "Hydrogen"]
