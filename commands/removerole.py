from discord import Interaction, Embed, Member, Role
from discord.app_commands import default_permissions
from util.functions import log

def commandFunction(tree, client):
    @tree.command(name= "removerole", description= "Remove a role from someone on your Discord server")
    @default_permissions(manage_roles = True)
    async def removeRoleCommand(interaction: Interaction, member: Member, role: Role):
        try:
            await member.remove_roles(role)
            embed = Embed(title=" ",description=f":white_check_mark: **Successfully removed** ``{role}`` **from** ``{member}``**.**",colour=5763719)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(SUCCESS) {interaction.user} REMOVED a role from {member} on {interaction.user.guild} ({interaction.user.guild.id})")
        except:
            embed = Embed(title=" ",description=f":x: **An error occured**",colour=15548997)
            await interaction.response.send_message(" ",embed=embed)

            log(f"(FAIL) {interaction.user} failed to use /removerole")
